//revenge of pancakes


#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T,l,c;
    string s;
    char a[2]={' ',' '};

//    freopen("B-large.in","r",stdin);
 //   freopen("a.out","w",stdout);

    cin>>T;
    for(int i=1;i<=T;i++){

        cin>>s;
        l = s.length();
        a[0] = ' ',a[1] = ' ';
        c = 0;
        a[0] = s[0];
        for(int j=1;j<l;j++){

            //to add into first row
            if(a[1] == ' ' && a[0] != s[j]){
                //add it a[1]
              //  cout<<"adding  a[1] with"<<s[j]<<endl;
                a[1] = s[j];

            }
            else if(a[1] != ' ' && a[1]!=s[j]){
                //process the a[0] and a[1]
               // cout<<"processing as "<<a[1]<<" not "<<s[j]<<endl;
                if(a[0]=='+' && a[1] == '-') c += 2;
                else if(a[0]=='-' && a[1] == '+') c += 1;

                        a[0] = '+';
                        if(s[j] == '+')
                            a[1] = ' ';
                        else
                            a[1] = s[j];
            }

           // cout << a[0]<<" "<<a[1]<<" s[j] "<<s[j]<<endl;
        }

        if(a[1] == ' '){
            if(a[0] == '-') c+=1;
        }
        else{
            if(a[0]=='+' && a[1]=='-') c+= 2;
            else if(a[0] == '-' && a[1] == '+') c+= 1;
        }

        cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}
