    #include <cstdio>
    #include <iostream>
    using namespace std;
    double ken[1001];
    double naomi[1001];
    double kenD[1001];
    double naomiD[1001];
    double kenW[1001];
    double naomiW[1001];
    int main(){
    int n;
    cin >> n;
    int bNum;
    int resultD;
    int resultW;
    for(int curr = 1;curr<=n;curr++){
     
    resultD = 0;
    cin >> bNum;
    resultW = bNum;
    for(int i=0;i<bNum;i++){
    cin >> naomi[i];
    naomiD[i] = naomi[i];
    naomiW[i] = naomi[i];
    }
    for(int i=0;i<bNum;i++){
    cin >> ken[i];
    kenD[i] = ken[i];
    kenW[i] = ken[i];
    }
     
    //War (Ken good)
    int iPt = 0;
    int jPt = 0;
    double diff = 0;
    double sDiff = -1;
    bool exist;
    for(int i=0;i<bNum;i++){
    exist = false;
    sDiff = -1;
    for(int j=0;j<bNum;j++){
     
    if(naomiW[j] == -1)
    continue;
     
    diff = kenW[i] - naomiW[j];
     
    //
    //cout << i << " " << j << ": " << diff << endl;
     
     
    if(diff > 0){
    exist = true;
    if(sDiff == -1){
    sDiff = diff;
    iPt = i;
    jPt = j;
    }
    else if(diff < sDiff){
    sDiff = diff;
    iPt = i;
    jPt = j;
    }
    }
     
    }
     
    //cal
    //cout << exist << endl;
     
    if (exist) {
    // cout << iPt << " " << jPt << endl;
     
    resultW--;
    kenW[iPt] = -1;
    naomiW[jPt] = -1;
    }
     
    }
     
     
     
    iPt = 0;
    jPt = 0;
    diff = 0;
    sDiff = -1;
     
    //Deceive (naomi good)
    for(int i=0;i<bNum;i++){
    exist = false;
    sDiff = -1;
    for(int j=0;j<bNum;j++){
     
    if(kenD[j] == -1)
    continue;
     
    diff = naomiD[i] - kenD[j];
     
    if(diff > 0){
    exist = true;
    if(sDiff == -1){
    sDiff = diff;
    iPt = i;
    jPt = j;
    }
    else if(diff < sDiff){
    sDiff = diff;
    iPt = i;
    jPt = j;
    }
    }
     
    }
     
    //cal
    if (exist) {
    resultD++;
    kenD[jPt] = -1;
    naomiD[iPt] = -1;
    }
     
    }
     
     
    printf("Case #%d: %d %d\n",curr,resultD,resultW);
    }
    }
