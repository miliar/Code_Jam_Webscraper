// cccode.cpp : Defines the entry point for the console application.
//

#include <cstdlib>
#include <vector>
#include <unordered_map>
#include <string>
#include <fstream>

using namespace std;


 
class Solution {
public:
    vector<int> findSubstring(string S, vector<string> &L) {
        
        vector<int> v_startpos;
        
        int wordlen = L[0].length();
        
        unordered_map<string, int> map_word_count;
        for(int i=0; i<L.size(); i++){
            if(map_word_count.find(L[i])!=map_word_count.end()){
                map_word_count[L[i]] ++;
            }
            else{
                map_word_count[L[i]] = 1;
            }
        }
        
        for(int offset=0; offset < wordlen; offset++){
            unordered_map<string,int> appeared_word_count;
            int total_count=0;
            int left=offset;
            for(int ptr=offset; ptr<=(int)S.length()-wordlen; ptr+=wordlen){
                string word = S.substr(ptr,wordlen);
                if(map_word_count.find(word)!=map_word_count.end()){
                    if(appeared_word_count.find(word)!=appeared_word_count.end()){
                        appeared_word_count[word] ++;
                    }
                    else{
                        appeared_word_count[word]=1;
                    }
                    
                    if(appeared_word_count[word] <= map_word_count[word]){
                        total_count ++;
                        if(total_count == L.size()){
                            string left_word = S.substr(left, wordlen);
						    while(appeared_word_count.find(left_word)==appeared_word_count.end()){
							    left += wordlen;
							    left_word = S.substr(left, wordlen);
						    }
                            v_startpos.push_back(left);
                        }
                    }
                    
                    if(total_count == L.size()){
                        while(appeared_word_count[word] > map_word_count[word]){
                            string left_word = S.substr(left, wordlen);
                            if(appeared_word_count.find(left_word)!=appeared_word_count.end()){
                                appeared_word_count[left_word] --;
                                if(appeared_word_count[left_word] < map_word_count[left_word])
                                    total_count --;
                            }
                            left += wordlen;
                        }
                    }
                }
            }

			if(total_count == L.size()){
				string left_word = S.substr(left, wordlen);
				while(appeared_word_count.find(left_word)==appeared_word_count.end()){
					left += wordlen;
					left_word = S.substr(left, wordlen);
				}
				if(v_startpos.size()>0&&v_startpos.back()!=left)
				    v_startpos.push_back(left);
			}
        }
        
        return v_startpos;
    }
};

int main()
{
	/*string text = "abababab";
	vector<string> L ;
	L.push_back("a");
	L.push_back("b");
	
	Solution slv;
	vector<int> ret = slv.findSubstring(text, L);*/

	ifstream infile ("A-large.in");
	ofstream out ("out.txt");

	int T, Smax;
	infile >> T;
	for (int citr = 0; citr < T; citr++)
	{
		infile >> Smax;
		string data;
		infile >> data;

		int extra=0;
		int sum=0;
		for (int sitr = 0; sitr < Smax+1; sitr++)
		{
			int digit = data[sitr]-'0';
			if(sum<sitr){
				extra += sitr-sum;
				sum  = sitr;
			}
			sum += digit;
		}

		out << "Case #"<<(citr+1)<<": " << extra << std::endl;
	}

	infile.close();
	out.close();

	return 0;
}

