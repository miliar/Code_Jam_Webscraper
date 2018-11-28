#include <iostream>
#include <set>
using namespace std;

int main(){
    int size,temp,last,itr,crntmMbr,count = 0;
    set <int> x;
    cin >> size;
    int *arr = new int[size];
    for (int i = 0; i < size; ++i) {
        cin >> arr[i];
    }
    for (int i = 0; i < size; ++i) {
        x.clear();
        itr = 0;
        if(arr[i] == 0){
            cout <<"Case #" << i+1 << ": " << "INSOMNIA" << endl;
            continue;
        }
      while(x.size() != 10) {
            itr++;
            crntmMbr = arr[i] * itr;
            do {
                temp = crntmMbr % 10;
                if(x.size() <= 9){
                    x.insert(temp);
                }
                else{
                    break;
                }
                crntmMbr /= 10;
            }while(crntmMbr != 0);

        }
        crntmMbr = arr[i] * itr;
        cout << "Case #" << i+1 << ": " << crntmMbr << endl;
    }

}