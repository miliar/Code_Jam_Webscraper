#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;
int quatMultiply(int a, int b){
    bool positive=true;
    if(a<0 && b<0){
        a*=-1;
        b*=-1;
    }
    if(a<0){
        positive=false;
        a*=-1;
    }
    if(b<0){
    positive=false;
        b*=-1;
    }
    if(a == 1){
        return (positive)? b : -b;
    }
    if(b == 1){
        return (positive)? a : -a;
    }
    if(a == b){
        return (positive)? -1 : 1;
    }
    if(a==2){
        if(b==3){
            return (positive)? 4 : -4;
        }
        else{
            return (positive)? -3 : 3;
        }
    }
    if(a==3){
        if(b==2){
            return (positive)? -4 : 4;
        }
        else{
            return (positive)? 2 : -2;
        }
    }
    if(a==4){
        if(b==2){
            return (positive)? 3 : -3;
        }
        else{
            return (positive)? -2 : 2;
        }
    }
    return 1;
}
int main(int argv, char * arguements[])
{
    fstream input;
    input.open(arguements[1]);
    int total;
    input >> total;
    for(int i=0; i<total; i++){
        string data;
        string written;
        int l;
        int x;
        input >> l;
        input >> x;
        if(x>12){
            x=12+(x%4);
        }
        input >> data;
        for(int i=0; i<x; i++){
            written+=data;
        }
        int *ijk = new int[written.length()];
        for(int i=0; i<written.length(); i++){
            ijk[i]=written[i]-'i' + 2;
        }
        int soFar=1;
        bool foundI=false;
        int iIndex=-1;
        for(int i=0; i<written.length(); i++){
            soFar=quatMultiply(soFar, ijk[i]);
            if(soFar==2 && !foundI){
                iIndex=i;
                foundI=true;
            }
        }
        //cout << iIndex << endl;
        string answer="NO";
        if(soFar==-1 && foundI){
            int soFarBack=1;
            for(int i=written.length()-1; i>=iIndex+2; i--){
                soFarBack=quatMultiply(ijk[i], soFarBack);
                if(soFarBack==4){
                    //cout << "!" << i << endl;
                    answer="YES";
                    break;
                }
            }
        }
        //cout << written << endl;
        delete[] ijk;
        cout << "Case #" << i+1 << ": " << answer << endl;
    }
    return 0;
}
