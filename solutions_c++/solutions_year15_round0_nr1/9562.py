#include "std_lib_facilities.h"


int main()
{
	int T = 0;
	cin >> T;
    string fname = "codejam2015_al.txt";
    ofstream ofs(fname.c_str());
	
    for(int i=0; i<T; ++i){
            int s_m = 0;
            cin >> s_m;
            
            vector<int> audience;
            
            string data;
            cin >> data;

            
            istringstream is(data);
            char c = '0';
            int n = 0;
            for(int i=0; i<s_m+1; ++i){
                is >> c;
                n = c - '0';
                audience.push_back(n);
            }
            
        
            int need = 0;
            int all_stand = 0;
            int need_friend = 0;
            
            vector<int> all_stands(s_m+1);
            
            for(int i=0; i<s_m+1; ++i){
                if(i==0){
                    need = 0;
                    all_stand += audience[0];
                    all_stands[0] = all_stand;
                }
                else {
                    need = i;
                    if(need > all_stands[i-1]){
                        need_friend += 1;
                        all_stand += 1;
                    }
                    all_stand += (audience[i]);
                    all_stands[i] = all_stand;
                }
            }
            
    
		ofs << "Case #" << i+1 << ": " << need_friend << endl;
    }
}
