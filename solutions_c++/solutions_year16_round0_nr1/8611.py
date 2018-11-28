#include <iostream>
#include <stdio.h>
using namespace std;

bool seen[10];// whether digit is seen
void resetSeen(){
    for (int i = 0; i < 10; i++){
        seen[i] = false;
    }
}


void applyToSeen(int at)
{
    while(at != 0){
//        cout << "inner loop at: " << at << endl;
        seen[at % 10] = true;
        at/=10;
    }

}

bool done(){ 
    for (int i = 0; i < 10; i++){
        if (!seen[i]){
//            cout << "failed on " << i << endl;
            return false;
        }
    }
  //  cout << "success!" << endl;
    return true;
}

int main(){

    int cases;
    int base, at;
    cin >> cases;
    for (int i=1; i <= cases; i++)
    {
        cin >> base;
        at = base;
  //      cout << "case " << i << "starting with " << base << endl;
        resetSeen();
        for(int j=1; j < 1000 && at > 0 ; j++)
        {
//            cout << "at:" << at << endl;
            applyToSeen(at);
            if(done())
            {
             //   printf("Case #%d: %d\n", i, j);
                cout << "Case #" << i << ": " << at << endl;
                break;
            }
            at += base;
        }
        if (!done())
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
    }        
    return 0;
}
