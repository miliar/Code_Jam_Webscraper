#include<iostream>
using namespace std;
int main(){
    int test,a[4][4],b[17],c,d,k;
    cin >> test;
    for(int tc=0;tc<test;tc++){
        for(int i=0;i<17;i++) b[i] =0;
        k=0;
        cin >> c;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++) cin >> a[i][j];
        for(int i=0;i<4;i++)
            b[a[c-1][i]] = 1;
        cin >> c;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++) cin >> a[i][j];
        for(int i=0;i<4;i++)
            if(b[a[c-1][i]] == 1)
                k++,d = a[c-1][i];
        cout << "Case #" << tc+1 << ": ";
        if(k>1) cout << "Bad magician!\n";
        else if(k==0) cout << "Volunteer cheated!\n";
        else cout << d << endl;
    }
    return 0;
}


        
