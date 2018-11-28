#include <iostream>
#include <algorithm>

using namespace std;

int kenWin(float naomi[],float ken[],int size){
        int win = 0;
            int nindex=0;
                int kindex=0;
                    while(nindex<size && kindex<size){
                                if(naomi[nindex]>ken[kindex]){
                                                kindex++;
                                                        } else {
                                                                        win++;
                                                                                    nindex++;
                                                                                                kindex++;
                                                                                                        }
                                    }
                        return win;
}

int naomiWin(float naomi[],float ken[], int size){
        int win = 0;
            int nindex=size-1;
                int kindex=size-1;
                    while(nindex>=0 && kindex>=0){
                                if(naomi[nindex]>ken[kindex]){
                                                win++;
                                                            kindex--;
                                                                        nindex--;
                                                                                } else {
                                                                                                kindex--;
                                                                                                        }
                                    }
                        return win;
}

int main(){
        int t;
            cin>>t;
                for(int n=1;n<=t;n++){
                            int size;
                                    cin>>size;
                                            float naomi[size];
                                                    float ken[size];
                                                            for(int i=0;i<size;i++){
                                                                            cin>>naomi[i];
                                                                                    }
                                                                    for(int i=0;i<size;i++){
                                                                                    cin>>ken[i];
                                                                                            }
                                                                            std::sort(naomi, naomi + size);
                                                                                    std::sort(ken, ken+size);
                                                                                            int nWin = naomiWin(naomi, ken,size);
                                                                                                    int kWin = kenWin(naomi, ken, size);
                                                                                                            cout<<"Case #"<<n<<": "<<nWin<<" "<<size-kWin<<endl;
                                                                                                                }
                    return 0;
}
