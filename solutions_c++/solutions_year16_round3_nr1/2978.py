#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int findBiggest(int* tab,int size){
    int result = 0;
    for(int i = 0; i < size; ++i){
        if (*(tab+i) > *(tab+result)){
            result = i;
        }
    }
    return result;

}

int equals_one(int* tab, int size){
    int result = 0;
    for(int i = 0; i < size; ++i){
        if (tab[i] == 1){
            result++;
        }
    }
    return result;
}

int main() {
    int nbTest;

    cin >> nbTest;

    for(int i = 0; i < nbTest; ++ i){

        cout << "Case #" << 1+i << ": ";

        int n;
        int total = 0;
        int partyMember[26] = {0};

        cin >> n;

        for(int j = 0; j < n; j++){
            cin >> partyMember[j];
            total += partyMember[j];
        }

        int parity = 1;

        while (total > 3){
            int j = findBiggest(partyMember,26);
            cout << char(j+'A');
            parity++;
            if (parity%2) cout << " ";
            --partyMember[j];
            --total;

        }

        if(total == 2){
            int j;
            j = findBiggest(partyMember,3);
            --partyMember[j];
            cout << char(j+'A');
            j = findBiggest(partyMember,3);
            --partyMember[j];
            cout << char(j+'A');


            cout << endl;
        }
        else {

            int j = findBiggest(partyMember, 3);
            --partyMember[j];
            cout << char(j + 'A');
            cout << " ";

            j = findBiggest(partyMember, 3);
            --partyMember[j];
            cout << char(j + 'A');
            j = findBiggest(partyMember, 3);
            --partyMember[j];
            cout << char(j + 'A');


            cout << endl;
        }






    }





    return 0;
}