#include<bits/stdc++.h>

using namespace std;

string str;
int main()
{

    int t,counti=1;
    /*ofstream out;
    ifstream inp;
    inp.open("A.in");
*/

   // out.open("out.txt");
    cin>>t;
    //inp >> t;


    while(t--)
    {
        long long n,i,j,req=0,curr=0,diff;

        cin>>n>>str;
       // inp>>n>>str;

        int len=str.length();

        curr+=str[0]-48;

        for(i=1;i<len;i++)
        {if(i<=curr)
        {
            curr+=str[i]-48;
        }

        else
        {   diff=i-curr;
            req+=diff;

            curr+=(str[i]-48)+diff;

        }


        }

          cout<<"Case #"<<counti<<": "<<req<<endl;
          //out<<"Case #"<<counti<<": "<<req<<endl;
        counti++;




    }


   // inp.close();
    //out.close();

}
