#include <vector>
#include <algorithm>
#include<string>
#include <iostream>

using namespace std;
string v;
int main()
{   // char *ptr;
    int numCase;
    cin >> numCase;
    int i, j, n,k;
    long long ans;
    char r;
    string str;
    int head;

    for (i = 0; i < numCase; i++)
    {
        head=1004;
        cin>>str;
        v[head]=str[0];
        for(j=1;j<str.size();j++){
            if(str[j]>=v[head])
            {
                head--;
                v[head]=str[j];//cout<<"v["<<head<<"]= "<<v[head]<<endl;
            }
            else{
                v[head+j]=str[j];//cout<<"v["<<head+j<<"]= "<<v[head+j]<<endl;
            }
        }


        cout << "Case #" << (i+1) << ": " ;
       // cout<<"hello "<<str.size()<<head;
        for(j=0,k=head;j<str.size();j++,k++){
             //cout<<"hello ";
            cout<<v[k];
            v[k]=0;
        }
        cout<<endl;
    }
    return 0;
}
