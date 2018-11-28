#include<iostream>
using namespace std;
int main(){
    int a1[4],a2[4];
    int t,tmp,m,chk,ans,c=0;
    cin >> t;
    while((t--)!=0){
        cin >> m;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
                cin >> tmp;
                if(i==m-1)
                    a1[j]=tmp;
        }
        chk=0;
        cin >> m;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
                cin >> tmp;
                if(i==m-1)
                for(int k=0;k<4;k++)
                    if(a1[k]==tmp){
                        chk++;
                        ans=k;
                    }
        }
        c++;
        if(chk==0)
            cout << "Case #"<< c <<": Volunteer cheated! "<< endl;
        else if(chk==1)
            cout << "Case #"<< c <<": "<<  a1[ans] <<endl;
        else
            cout << "Case #"<< c <<": Bad magician! "<< endl;

    }
    return 0;

}
