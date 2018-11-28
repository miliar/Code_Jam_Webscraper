#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int t;
    FILE *in,*o;
    o = fopen ("output.txt","w");
    cin>>t;
    int n1,n2;
    int a[5][5];
    int temp1[5];
    int temp2[5];
    int count = 0;
    int ans;
    int k =1;
    while (k<=t){
            count = 0;
            cin>>n1;
        for (int i=1; i<=4; i++){
            for (int j=1; j<=4; j++){
                cin>>a[i][j];
            }
        }
        int j;
        for (int i=1; i<=4; i++){
            j = n1;
            temp1[i] = a[j][i];
        }
        cin>>n2;
        for (int i=1; i<=4; i++){
            for (int j=1; j<=4; j++){
                cin>>a[i][j];
            }
        }
         for (int i=1; i<=4; i++){
            j = n2;
            temp2[i] = a[j][i];
        }

        for (int i=1; i<=4; i++){
                for (int k=1; k<=4; k++){
                    if (temp1[i] == temp2[k]){
                        ans = temp1[i];
                        count++;
                    }
                }
        }
        if (count==1){
            fprintf(o,"Case #%d: %d\n",k,ans);
        }
        else if (count==0){
            fprintf(o,"Case #%d: Volunteer cheated!\n",k);
        }
        else if(count > 1){
            fprintf(o,"Case #%d: Bad magician!\n",k);
        }
        k++;
    }
return 0;
}

