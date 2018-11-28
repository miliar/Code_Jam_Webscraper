#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large (1).in","r",stdin);
	freopen("output1.out","w",stdout);
    int t,ti,i;
    char str[1000];
    cin>>t;
    for(ti=1;ti<=t;ti++)
    {
        cout<<"Case #"<<ti<<": ";
        vector<char> vec;
        cin>>str;
        vec.push_back(str[0]);
        for(i=1;str[i];i++)
        {
            if(str[i]>=vec[0])
            {
                vec.insert(vec.begin(), str[i]);
            }
            else
            {
                vec.push_back(str[i]);
            }
        }
        vector<char>::iterator itr=vec.begin();
        while(itr!=vec.end())
        {
            cout<<*itr;
            itr++;
            
        }
        cout<<endl;
    }
    
	return 0;
}

