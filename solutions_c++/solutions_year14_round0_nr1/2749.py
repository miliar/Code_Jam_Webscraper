#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(void) {
    unsigned short int t;
    int n1,n2;
    int a[4][4],temp1[4],temp2[4];
    cin >> t;
    for(int c=1;c<=t;c++)
    {
        cin>>n1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];

        for(int i=0;i<4;i++)
        {
            temp1[i]=a[n1-1][i];
          //  cout<<temp1[i]<< " ";
        }
        //cout<< endl;
        cin>>n2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        for(int i=0;i<4;i++)
        {
            temp2[i]=a[n2-1][i];
            //cout<<temp2[i]<< " ";
        }
        //cout<<endl;
        int comm[4],index=0;
        for(int i=0;i<4;i++)
            comm[i]=-1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                if(temp1[i]==temp2[j])
                {
                    comm[index]=temp1[i];
                    index++;
                }
            }
       if(index==1)
            cout << "Case #" << c << ": " << comm[0] << endl;
        if(index>1)
            cout << "Case #" << c << ": " << "Bad magician!" << endl;
        if(index<1)
            cout << "Case #" << c << ": " << "Volunteer cheated!" << endl;

    }

    return 0;
}