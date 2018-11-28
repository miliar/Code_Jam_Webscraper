#include <iostream>
#include <string>

using namespace std;

const int CACHE_LEN = 10;	// ASSERT CACHE_LEN > 1
const int MAX_CACHE = 1024;	// ASSERT MAX_CACHE > 4
const int TWO_ARRAY[] = {1,2,4,8,16,32,64,128,256,512,1024,
		2048};
int cache[MAX_CACHE] = {0, 0, 0, 1};	// {unuse, unuse, +, -}

void calculateCache(){
	// interval start, mid, end point
	int i_start = 4, i_mid = 6, i_end = 8;
	for(int i=4; i<MAX_CACHE; i++){
		if(i == i_end){
			i_start = i_start * 2;
			i_mid = i_mid * 2;
			i_end = i_end * 2;
		}
		
		if(i<i_mid){
			cache[i] = cache[i-i_start/2];
		}
		else{
			cache[i] = 1+cache[2*i_mid-i-1];
		}
	}
}

int getBlockFlipCount(string block_s){
	int idx_block_res = 1;
	for(int i=0; i<block_s.length(); i++){
		if(block_s[i] == '+'){
			idx_block_res += TWO_ARRAY[i];
		}
		else{
			idx_block_res += TWO_ARRAY[i+1];
		}
	}
	//cout << block_s << " " << idx_block_res << " " <<
	//cache[idx_block_res] << endl;
	return cache[idx_block_res];
}

string doSignChangeString(string s){
	string r = "";
	for(int i=0; i<s.length(); i++){
		if(s[i] == '+') r += '-';
		else r += '+';
	}
	return r;
}

int useCacheSearch(string s){
	int rear = s.length()-1;
	int i,lastChar, isChanged = 0;
	if(s[rear] == '+') lastChar = -1;
	else lastChar = -2;
	
	for(i=rear; i>=0; i--){
		if(isChanged == 0){
			if(s[i] != s[rear]){
				isChanged = 1;
				break;
			}
		}
	}
	
	if(isChanged == 0) return lastChar;
	else if(i <= rear - CACHE_LEN + 1) return i;
	else{
		for(int j=rear - CACHE_LEN+2; j<rear; j++){
			if(s[j] == '+') return j;
		}
		return i+1;
	}
}

int getFlipCount(string s){
	// translate string to number
	int slen = s.length();
	int block_slen = 0;
	string block_s;
	int result = 0;
	
	while(slen > 0){
		if(slen < CACHE_LEN){	// no need to split string
			block_s = s;
			result += getBlockFlipCount(block_s);
			break;
		}
		else{	// need to split string
			// how to find string splitting point?
			// ~() operation means + to -, - to + (sign change)
			// 1. pattern1 + all '+' -> cost(pattern1)
			// 2. pattern1 + all '-' -> cost(~(pattern1))+1
			// 3. how to reuse cache?
			
			int k = useCacheSearch(s);
			//cout << "check0:"<< k << endl;
			
			if(k == -1){
				result += 0;
				slen = 0;
			}
			else if(k == -2){
				result += 1;
				slen = 0;
			}
			else{
				if(k <= slen - CACHE_LEN){
					if(s[slen-1] == '-') result += 1;
					slen = k+1;
					s = s.substr(0, slen);
				}
				else{
					block_s = s.substr(k, slen - k);
					result += getBlockFlipCount(block_s);
					slen = k;
					s = s.substr(0, slen);
				}
			}
		}
	}
	return result;
}

int main(){
    int t;
    string s;
    int r=0;
    
    cin >> t;
    // use pre-calculation to CACHE_LEN-1
    calculateCache();
    
    for(int i=1; i<=t; ++i){
        // read input
        cin >> s;
        
        // calculate algorithm
        r = getFlipCount(s);

        // print result
        cout << "Case #" << i << ": " << r << endl;
    }
    return 0;
}
