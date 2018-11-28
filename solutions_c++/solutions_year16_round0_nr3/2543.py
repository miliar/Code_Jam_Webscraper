#include<iostream>
#include<string>
#include<vector>
using namespace std;

int N, J;
long long bs[16][11];

void recur(int level, long long nums[11], char jc[16]){
    if(level == 0){
	vector<long long> divs;
	jc[level] = '1';
	for(int i=2; i<11; ++i){
	    nums[i] += bs[level][i];
	}
	for(int i=2; i<11; ++i){
	    // check num[i]
	    if(nums[i] % 2 == 0){
		divs.push_back(2);
	    }else if(nums[i] % 3 == 0){
		divs.push_back(3);
	    }else{
		long long tt = 5;
		while(tt*tt <= nums[i]){
		    if(nums[i] % tt == 0){
			divs.push_back(tt);
			break;
		    }else if(nums[i] % (tt+2) == 0){
			divs.push_back(tt+2);
			break;
		    }
		    tt += 6;
		}
		if(tt*tt > nums[i]){
		    break;
		}
	    }
	}
	// check, if Y -> J-1
	if(divs.size() == 9){
	    cout << string(jc);
	    for(long long d: divs){
		cout << " " << d;
	    }
	    cout << endl << flush;
	    --J;
	}
	for(int i=2; i<11; ++i){
	    nums[i] -= bs[level][i];
	}
	return;
    }
    // bit = 0
    jc[level] = '0';
    recur(level-1, nums, jc);
    if(J == 0) return;
    // bit = 1
    jc[level] = '1';
    for(int i=2; i<11; ++i){
	nums[i] += bs[level][i];
    }
    recur(level-1, nums, jc);
    for(int i=2; i<11; ++i){
	nums[i] -= bs[level][i];
    }
    return;
}

int main(){
    for(int i=2; i<11; ++i)	bs[15][i] = 1;
    for(int j=14; j>=0; --j){
	for(int i=2; i<11; ++i){
	    bs[j][i] = bs[j+1][i] * i;
	}
    }
    int T;
    cin >> T;
    for(int t=1; t<=T; ++t){
	cin >> N >> J;
	cout << "Case #" << t << ":" << endl;
	long long nums[11];
	char jc[17];
	jc[16] = '\0';
	for(int i=2; i<11; ++i){
	    nums[i] = 1;
	}
	jc[N-1] = '1';
	recur(N-2, nums, jc);
    }
    return 0;
}
