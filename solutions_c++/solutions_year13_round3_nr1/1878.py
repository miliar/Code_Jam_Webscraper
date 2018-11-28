#include<iostream>
#include<string>

using namespace std;


int main()
{
    int t;
    cin>>t;

    for(int cas=1; cas<=t; cas++)
    {
        string s;
        int n;
        cin>>s>>n;
        int count = 0;
        int size = s.length();

        for(int len=n; len<=size; len++)
        {
            for(int i=0; (i+len)<=size; i++)
            {
                string s2 = s.substr(i, len);

                bool f = false;

                for(int k=0; (!f)&&(s2[k+n-1]!='\0'); k++)
                {

                    int i2;
                    for(i2=k; i2 <= k+n-1 ; i2++)
                    {
                        char c = s2[i2];
                        if((c=='a')||(c=='e')||(c=='i')||(c=='o')||(c=='u'))
                            break;
                    }

                    if(i2 > k+n-1)
                        f=true;
                }


                if(f)
                {count++;
                //cout<<s2<<endl;
                }
            }
        }
        cout<<"Case #"<<cas<<": "<<count<<endl;
    }
}
