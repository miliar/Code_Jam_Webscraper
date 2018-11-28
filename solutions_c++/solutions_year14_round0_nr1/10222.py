 #include <iostream>
    #include <stdio.h>
    #include <vector>
    #include <set>
    #include <cstdlib>
    #include <math.h>
    #include <string>
    #include <map>
    #include <algorithm>
    using namespace std;
    #define READ(s) freopen(s, "r", stdin)
    #define WRITE(s) freopen(s, "w", stdout)

    int main() {
    READ("A-small-attempt2.in");
    WRITE("A-small-attempt2.out");
    int t,x,y,n[5][5],m[5][5],index,counter=0;
    cin>>t;
    for(int i=0;i<t;i++){
    counter=0;
    cin>>x;
    for(int a=1;a<5;a++){
    for(int b=1;b<5;b++){
    cin>>n[a][b];
    }
    }
    cin>>y;
    for(int a=1;a<5;a++){
    for(int b=1;b<5;b++){
    cin>>m[a][b];
    }
    }
    for(int a=1;a<5;a++){
    for(int b=1;b<5;b++){
    if(n[x][a]==m[y][b]){
    counter++;
    index=b;
    }
    }
    }
    if(counter==0){
    cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    }
    else if(counter==1){
    cout<<"Case #"<<i+1<<": "<<m[y][index]<<endl;
    }
    else {
    cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    }

    }


    return 0;
    }



