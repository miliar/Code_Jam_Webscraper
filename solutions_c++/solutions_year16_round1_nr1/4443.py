#include <iostream>
#include<vector>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    int test;
    int l;
    cin>>test;
    string s;
    vector<char> vec;
    int i,j;
    vector<char>::iterator it;
    for(j=1;j<=test;j++){
        cin>>s;
        l=s.length();
        vec.push_back(s[0]);
        for(i=1;i<l;i++){
            it=vec.begin();
            if(s[i]>=vec[0]){
                vec.insert(it,s[i]);
            }
            else{
                vec.push_back(s[i]);
            }
        }
        cout<<"Case #"<<j<<": ";
        for(i=0;i<l;i++)
            cout<<vec[i];
        cout<<endl;
        vec.clear();
    }
    return 0;
}

