#include <bits/stdc++.h>
#define ll long long
#define ff first
#define ss second
#define mp make_pair
using namespace std;

set<pair<int , int> > s;

int main(){

    freopen("A-large.in" , "r" , stdin);
    freopen("dream.out" , "w" , stdout);
    int t , z = 1;
    cin >> t;
    while(t--){
        s.clear();
        int n;cin >> n;
        printf("Case #%d: " , z++);
        int sum = 0;
        for(int i = 0; i < n; ++i){
            int tmp;
            cin >> tmp;
            sum += tmp;
            s.insert(mp(-tmp , i));
        }

        while(!s.empty()){

            pair<int, int> fi , se;
            fi = *s.begin();
            s.erase(s.begin());
            se = *s.begin();
            s.erase(s.begin());


            if((-1*fi.first) > 1 && (-1*se.first)*2 <= (sum-2)){

                fi.first += 2;
                printf("%c%c " , fi.second+'A' , fi.second+'A');
                sum -= 2;


            }

            else if(((-1*fi.first) -1)*2 <= (sum-2) && ( (-1*se.first)-1)*2 <= (sum-2) ){

                if(s.size() != 1){
                    fi.first += 1;
                    se.first += 1;
                    printf("%c%c " , fi.second+'A' , se.second+'A');
                    sum -= 2;
                }else {

                    pair<int, int> th;
                    th = *s.begin();
                    s.erase(s.begin());

                    if( (-1*th.first)*2 <= (sum-2) ){

                        fi.first += 1;
                        se.first += 1;
                        printf("%c%c " , fi.second+'A' , se.second+'A');
                        sum -= 2;
                    }else{
                        fi.first += 1;
                        printf("%c " , fi.second+'A');
                        sum -= 1;

                    }

                    s.insert(th);


                }



            }

            else{

                fi.first += 1;
                printf("%c " , fi.second+'A' , se.second+'A');
                sum -= 1;


            }


            if(fi.first != 0){
                s.insert(fi);
            }

            if(se.first != 0){
                s.insert(se);
            }



        }

        cout << "\n";


    }
    return 0;
}
