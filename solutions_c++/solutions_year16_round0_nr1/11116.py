#include <iostream>

using namespace std;

long countSheep(long B){
    bool flags[10] = {false,false,false,false,false,false,false,false,false,false};
    int flagsSet = 0;
    long i = 0;
    long C;
    if(B==0){
        return 0;
    }
    while(flagsSet < 10){
        i++;
        C = B*i;

        do {
            int digit = C % 10;
            if(!flags[digit]){
                flags[digit] = true;
                flagsSet++;
            }
            C /= 10;
        } while (C > 0);
    }
    return B*i++;
}


int main(void) {
    int T;
    cin>>T;
    long B[T];

    int i;
    
    for (i = 0; i < T; ++i)
    {
        cin>>B[i];   
    }

    long result;
    for (i = 0; i < T; ++i)
    {
        result = countSheep(B[i]);
        if(result != 0){
            cout<<"Case #"<<(i+1)<<": "<<result<<endl; 
        }
        else{
            cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
        }
    }

    return 0;
}
