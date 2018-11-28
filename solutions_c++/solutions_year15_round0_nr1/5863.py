#include<iostream>
#include<stack>
#include <sstream>
using namespace std;

void input() {

    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

}

int main(void)
{

    input();

    int t;
    cin>>t;
    int j=1;
    while(j<=t)
    {
        int s;
        int cu=0,c=0;
        cin>>s;
        char in[10002];

        cin>>in;

        for(int i=0;i<=s;i++)
        {
            int temp= in[i] - '0';

            if(i<=cu)
            {
                cu=cu+temp;
            }
            else
            {
                int dif=i-cu;
                c=c+dif;
                cu=cu+temp+dif;
            }

        }

        cout<<"Case #"<<j<<": "<<c<<endl;
        j++;
    }

    return 0;
}
