#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.in","w",stdout);
    int cases;
    cin>>cases;
    int temp =0;
    while(cases--)
    {
                  temp++;
    string a;
    string b ="";
    cin>>a;
    for(int i=0;i<a.length();i++)
    {
            if(a[i]=='a'||a[i]=='u'||a[i]=='o'||a[i]=='i'||a[i]=='e')
            {
                   b =b + '0';
            }
            else
            {
                  b =b+'1';
            }
    }                                                         
    int num,ptr,counter=0;
    long long int ans =0;
    scanf("%d",&num);
    long long int step;
   // cout<<b;
   
    for(int i=0;i<b.length();i++)
    {
            
            ptr =i;
            counter =0;
             step=0;
            for(int j = i; j<b.length();j++)
            {
                     if(counter!=num)
                     {
                          if(b[j]=='1')
                          {
                             //step++;
                               counter++;
        //                       cout<<"a"<<counter<<"j"<<j<<endl;
                          }
                          else
                          {
                             counter =0;   
                          }
                             
                     }
                     else
                     {
      //                   cout<<"counter"<<counter<<"ans"<<ans<<endl;
                        ans =  ans +  1 +  b.length() - j;
          //              cout<<ans<<endl;
                        break;
                     }
                     if(counter==num&&j==(b.length()-1))
                           {
                                     ans = ans + 1;
                            }
            //         cout<<"abc"<<ans<<endl;
            }
            //cout<<"out"<<endl;
    }
    cout<<"Case #"<<temp<<": "<<ans<<endl;
    }        
    //system("pause");
    return 0;
}
 
