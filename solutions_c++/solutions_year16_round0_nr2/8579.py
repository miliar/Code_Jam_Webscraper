#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
    freopen("input.txt" , "r" , stdin) ;
    freopen("output.txt" , "w" , stdout) ;

    int t , CASE = 0 ;
    string s ;
    cin >> t ;
    while(t--){
        cin >> s ;
        int i , ret = 0 , l = s.size() ;
        queue <char> st ;
        for(i = 0 ; i < l ; i++){
            st.push(s[i]) ;
        }
//            queue<char>st2 ; st2 = st ;
//            while(st2.size()!=0){
//                cout<<st2.front();st2.pop();
//            }
//            cout<<endl;

        while(true){
            int x = 0 ;
            int mns = 0 , pls = 0 ;
            char c ;
            while(st.size() != 0){
                c = st.front() ;
                if(pls == 0 && mns ==0){
                    if(c == '+')    pls++ ;
                    else    mns++ ;
                }
                else if(pls == 0){
                    if(c == '+')    break ;
                    else    mns++ ;
                }
                else if(mns == 0){
                    if(c == '+')    pls++ ;
                    else    break ;
                }
                st.pop() ;
            }

            if(pls >= l){
                break;
            }
            else{
                int k = max(pls,mns) ;
                for(i = 0 ; i < k ; i++)    st.push('+') ;
                ret++ ;
            }

//            queue<char>st2 ; st2 = st ;
//            while(st2.size()!=0){
//                cout<<st2.front();st2.pop();
//            }
//            cout<<endl;
        }

        cout <<"Case #"<<++CASE<<": " << ret << endl ;
    }
}

