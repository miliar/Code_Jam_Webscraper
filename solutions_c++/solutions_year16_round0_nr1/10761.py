#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;
int main()
{
    int t;
    cin >>t;
    for(int i=0;i<t;i++)
    {
    int num;
    stringstream ss1;

        int num_array[10];
        for(int k=0;k<10;k++)
            num_array[k]=0;
        cin >> num;
            for(int k=0;k<10;k++)
                num_array[k]=0;

             int sum=0;
             int oldnum=num;
             do{
                 sum=0;
        //        cout<<"num: "<<num<<endl;
                 string n;

                 ss1 << num;
                 n=ss1.str();
          //           cout<<"n: "<<n<<endl;
                 
                         for(char &c : n){
            //                 cout<<"c: "<<c<<endl;
                             if(c=='0' && num_array[0]==0)
                                 num_array[0]=1;
                             if(c=='1' && num_array[1]==0)
                                 num_array[1]=1;
                             if(c=='2' && num_array[2]==0)
                                 num_array[2]=1;
                             if(c=='3' && num_array[3]==0)
                                 num_array[3]=1;
                             if(c=='4' && num_array[4]==0)
                                 num_array[4]=1;
                             if(c=='5' && num_array[5]==0)
                                 num_array[5]=1;
                             if(c=='6' && num_array[6]==0)
                                 num_array[6]=1;
                             if(c=='7' && num_array[7]==0)
                                 num_array[7]=1;
                             if(c=='8' && num_array[8]==0)
                                 num_array[8]=1;
                             if(c=='9' && num_array[9]==0)
                                 num_array[9]=1;
                         }
//             cout<<"num: "<<num<<endl;
             num=num+oldnum;
             ss1.clear();
//             cout<<sum<<endl;
                     for(int j=0;j<10;j++)
                         sum=sum+num_array[j];
             if(num==0)
                 sum=10;
             }while(sum!=10);
             if(sum==10&&num!=0)
                 cout<<"Case #"<<i+1<<": "<<num-oldnum<<endl;
             else if(sum==10 && num==0)
                 cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
      
    }
    return 0;
}
            


