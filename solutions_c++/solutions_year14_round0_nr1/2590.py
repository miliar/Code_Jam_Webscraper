#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    freopen("t.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int T,choice,temp,res,ans;
    cin >> T;
    for(int t=0;t<T;t++){
        int A[16]={0};
        cin >> choice;
        for(int i=0;i<16;i++){
            cin >> temp;
            if(i<(choice)*4 && i>=(choice-1)*4)
                A[temp-1]++;
        }
        cin >> choice;
        for(int i=0;i<16;i++){
            cin >> temp;
            if(i<(choice)*4 && i>=(choice-1)*4)
                A[temp-1]++;
        }
        res=0;
        for(int i=0;i<16;i++){
            if(A[i]>=2){
                res++;
                ans=i+1;
            }
        }
        if(res==1){
            printf("Case #%i: %i\n",t+1,ans);
        } else if(res>1){
            printf("Case #%i: Bad magician!\n",t+1);
        } else {
            printf("Case #%i: Volunteer cheated!\n",t+1);
        }
    }
    return 0;
}
