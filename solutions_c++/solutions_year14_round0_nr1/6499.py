#include <iostream>

using namespace std;

int main()
 {
    int a1,a2,t,i,j,k,l,index;

    int num_xor=0,testcase;
    cin>>t;
    for(testcase=1;testcase<=t;testcase++)
     {
        int ar1[4][4],ar2[4][4];
        num_xor=0;
        cin>>a1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>ar1[i][j];
        cin>>a2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>ar2[i][j];
        i=a1-1;
        k=a2-1;
        for(j=0;j<4;j++)
         {
            for(l=0;l<4;l++)
             {
                if(ar1[i][j]==ar2[k][l])
                 {
                    if(num_xor==0)
                     {
                        index=j;
                     }
                     num_xor++;
                 }
             }
         }

        if(num_xor>1)
         {
            cout<<"Case #"<<testcase<<": Bad magician!"<<endl;
         }
        else if(num_xor==1)
         {
            cout<<"Case #"<<testcase<<": "<<ar1[a1-1][index]<<endl;
         }
        else if(num_xor==0)
         {
            cout<<"Case #"<<testcase<<": Volunteer cheated!"<<endl;
         }

     }

    return 0;
 }
