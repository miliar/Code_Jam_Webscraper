#include<bits/stdc++.h>
using namespace std;

set<int> st;
int main()
{
    int T,N,z,c=1;
    cin>>T;
    while(T--)
    {
        cin>>N;
        st.clear();
        for(int i=1;i<=1000;++i)
        {
            z = N*i;
            while(z){
                st.insert(z%10);
                z/=10;
            }
            if(st.size()==10){
                cout<<"Case #"<<c++<<": "<<N*i<<endl;
                break;
            }
        }
        if( st.size()!=10 )
        {
            cout<<"Case #"<<c++<<": INSOMNIA"<<endl;
        }
    }
}

