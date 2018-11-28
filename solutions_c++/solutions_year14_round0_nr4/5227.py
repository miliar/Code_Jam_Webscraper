     #include <iostream>
    #include <algorithm>
    using namespace std;
     
    int main() {
    int Tet, note, iot, jot, cWar, cfulWar;
    float kapil[1000], kavish[1000];
    cin>>Tet;
    for(int yumtu=1;yumtu<=Tet;++yumtu){
    cin>>note;for(iot=0;iot<note;++iot) cin>>kapil[iot];
              for(iot=0;iot<note;++iot) cin>>kavish[iot];
    
    
    sort(kavish,kavish+note);
    iot=0,jot=0;
    cfulWar=0;
    sort(kapil,kapil+note);
    
    
    while(iot<note){
    if(kapil[iot]>kavish[jot]){
    cfulWar++;
   
    jot++;
   
    }
    iot++;
    }
    cWar=0;
    
    iot=0,jot=0;
    
    while(iot<note){
    if(jot==note) break;
    if(kapil[iot]<kavish[jot]){
    iot++;
    
    cWar--;
    
    }
    jot++;
    }
   
                              cWar+=note;
   
    cout<<"Case #"<<yumtu<<": "<<cfulWar<<" "<<cWar<<endl;
    }
    return 0;
    }
