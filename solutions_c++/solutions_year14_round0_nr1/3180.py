#include <iostream>

using namespace std;

int main()
{
    int t,x,y;
    int first[4];
    int second[4];
    int temp[4];
    cin >> t;
    for(int i=0;i<t;i++) {
        //nie chce mi sie teraz funkcji robiæ
        cin>>x;
        for(int j=0;j<4;j++) {
            int k;
            for(k=0;k<4;k++) {
                cin>>temp[k];
            }
            if((j+1)==x) for(k=0;k<4;k++) first[k]=temp[k];
        }
        cin>>y;
        for(int j=0;j<4;j++) {
            int k;
            for(k=0;k<4;k++) {
                cin>>temp[k];
            }
            if((j+1)==y) for(k=0;k<4;k++) second[k]=temp[k];
        }

        int karta=0;
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                if(first[j]==second[k]) {
                    if(karta==0) karta=first[j]; else { karta=17; break; }
                }
            }
            if(karta==17) break;
        }

        if(karta==0) cout<< "Case #" << i+1 <<": Volunteer cheated!";
        else if(karta==17) cout << "Case #" << i+1 <<": Bad magician!";
        else cout << "Case #" << i+1 <<": " << karta;

        if((i+1)<t) cout << endl;
    }
    return 0;
}
