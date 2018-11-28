// C++11
#include <iostream>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <functional>
#include <set>
#include <map>

using namespace std;


void test_large(){

}

void test_small(){

    int T;

    cin>>T;


    for(int c=1; c<=T; c++){

        string s;
        cin>>s;

        vector<int> digits(10, 0);

        vector<string> digs = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

        int n = s.size();


        vector<int> num_d(26, 0);


        for(int i=0; i<n; i++){

            num_d[s[i]-'A']++;
        }

        vector<int> nums;

        int idx =0;

        for(int i=0; i<n; i++){

            if(s[i] == 'Z'){

                for(int j=0; j<digs[0].size(); j++){
                    num_d[digs[0][j]-'A']--;
                }

                nums.push_back(0);
            }

            if(s[i] == 'X'){

                for(int j=0; j<digs[6].size(); j++){
                    num_d[digs[6][j]-'A']--;
                }

                nums.push_back(6);
            }

            if(s[i] == 'W'){

                idx = 2;

                for(int j=0; j<digs[idx].size(); j++){
                    num_d[digs[idx][j]-'A']--;
                }

                nums.push_back(idx);
            }

            if(s[i] == 'G'){

                for(int j=0; j<digs[8].size(); j++){
                    num_d[digs[8][j]-'A']--;
                }

                nums.push_back(8);
            }


        }



        for(int i=0; i<26; i++){


                if(i == ('S' - 'A') ){

                    int nn = num_d[i];

                    for(int k=0; k<nn; k++){

                        idx = 7;

                        for(int j=0; j<digs[idx].size(); j++){
                            num_d[digs[idx][j]-'A']--;
                        }

                        nums.push_back(idx);
                    }


                }

        }


        for(int i=0; i<26; i++){



                if(i == ('V' - 'A') ){
                    int nn = num_d[i];

                    for(int k=0; k<nn; k++){

                        idx = 5;

                        for(int j=0; j<digs[idx].size(); j++){
                            num_d[digs[idx][j]-'A']--;
                        }

                        nums.push_back(idx);
                    }


                }

        }

        for(int i=0; i<26; i++){

            //if(num_d[i] > 0){

                if(i == ('F' - 'A') ){

                    int nn = num_d[i];

                    for(int k=0; k<nn; k++){
                        idx = 4;

                        for(int j=0; j<digs[idx].size(); j++){
                            num_d[digs[idx][j]-'A']--;
                        }

                        nums.push_back(idx);
                    }


                }
           // }
        }


        for(int i=0; i<26; i++){



                if(i == ('T' - 'A') ){

                    int nn = num_d[i];

                    for(int k=0; k<nn; k++){
                        idx = 3;

                        for(int j=0; j<digs[idx].size(); j++){
                            num_d[digs[idx][j]-'A']--;
                        }

                        nums.push_back(idx);
                    }


                }

        }


        for(int i=0; i<26; i++){



                if(i == ('O' - 'A') ){

                    int nn = num_d[i];

                     for(int k=0; k<nn; k++){
                         idx = 1;

                         for(int j=0; j<digs[idx].size(); j++){
                             num_d[digs[idx][j]-'A']--;
                         }

                         nums.push_back(idx);
                     }


                }

        }


        for(int i=0; i<26; i++){



                if(i == ('I' - 'A') ){
                    int nn = num_d[i];

                     for(int k=0; k<nn; k++){
                         idx = 9;
                         for(int j=0; j<digs[idx].size(); j++){
                             num_d[digs[idx][j]-'A']--;
                         }

                         nums.push_back(idx);

                     }


                }

        }


        sort(nums.begin(), nums.end());

        string rep(nums.size(), '0');

        for(int i=0; i<nums.size(); i++){
            rep[i] = '0' + nums[i];
        }

        cout<<"Case #"<<c<<": "<<rep<<endl;
    }


}

int main()
{
    test_small();
    return 0;
}

