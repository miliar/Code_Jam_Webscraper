#include <iostream>

using namespace std;

int main()
{
    int n;
    int row1,row2,base;
    int r1[4],r2[4];
    cin>>n;
    int temp, k=0;
    for(int i=0; i<n ;i++){
        cin>>row1;
        base=(row1-1)*4;
        k=0;
        while(cin>>temp){
          if(k>=base && k<base+4)
                r1[k-base]=temp;
           if(k==15)
                break;
           k++; 
        }
        cin>>row2;
        base=(row2-1)*4;
        k=0;
        while(cin>>temp){
          if(k>=base && k<base+4)
                r2[k-base]=temp;
           if(k==15)
                break;
           k++; 
        }
        k=0;
        int key;
        for(int j=0; j<=3; j++){
            for(int l=0; l<=3; l++){
                if( r1[j]==r2[l]){
                    k++;
                    key=r1[j];
                }
            }
        }
        if(k==0)
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        else if(k==1)
            cout<<"Case #"<<i+1<<": "<<key<<endl;
        else
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    }
    return 0;
}
