#include <iostream>
#include <vector>
#include <string>

using namespace std ;
int main(){
        int times = 100;
        int toplam = 101;
        while(times){
            vector <int> first_deck(4);
            vector <int> second_deck(4);
            int the_number;
            cin >> the_number;
            for (int i=0; i<4; i++) {
                if (i == the_number-1)
                {
                    cin >> first_deck[0];
                    cin >> first_deck[1];
                    cin >> first_deck[2];
                    cin >> first_deck[3];
                }
                else {
                    for (int k = 0; k<4; k++) {int he;cin>> he ;}}
            }
            cin >> the_number;
            for (int i=0; i<4; i++) {
                if (i == the_number-1)
                {   cin >> second_deck[0];
                    cin >> second_deck[1];
                    cin >> second_deck[2];
                    cin >> second_deck[3];
                }
                else {
                    for (int k = 0; k<4; k++) {int he;cin>> he ;}}
            }
            int result = 0;
            int the_card;
            for (int i=0; i<4; i++) {
                for (int j=0; j<4; j++) {
                    if(first_deck[i] ==second_deck[j]  )
                    {
                        result++ ;the_card = first_deck[i];
                    }
                }
            }
            first_deck.clear();
            second_deck.clear();
            if (result == 0)
                cout <<"Case #"<<(toplam-times)<<": "<< "Volunteer cheated!"<<endl;
            else if(result == 1)
                cout <<"Case #"<<(toplam-times)<<": "<< the_card<<endl;
            else
                cout<<"Case #"<<(toplam-times)<<": " << "Bad magician!"<<endl;
            times--;
        }
    
    
    return 0;
}