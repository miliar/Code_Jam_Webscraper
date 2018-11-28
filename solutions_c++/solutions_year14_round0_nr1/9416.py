#include <iostream>

using namespace std;

void apply(){
    int n,i,a[4],b[4],l,tmp,cnt;
    i=1;
    cnt=0;
    cin >> n;
    while(i<5){
        if(i==n)
            cin >> a[0] >> a[1] >> a[2] >> a[3];
        else
            cin >> l >> l >> l >> l;
        i++;
    }
    i=1;
    cin >> n;
    while(i<5){
        if(i==n)
            cin >> b[0] >> b[1] >> b[2] >> b[3];
        else
            cin >> l >> l >> l >> l;
        i++;
    }
    for(i=0;i<4;i++){
        for(l=0;l<4;l++){
            if(a[i]==b[l]){
                tmp = a[i];
                cnt++;
            }
        }
    }
    if(cnt==0){
        cout << "Volunteer cheated!" << endl;
    }
    else if(cnt==1){
        cout << tmp << endl;
    }
    else{
        cout << "Bad magician!" << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        cout << "Case #" << i << ": ";
        apply();
    }
   return 0;
}