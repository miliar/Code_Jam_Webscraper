#include <iostream>
#include <fstream>
using namespace std;

ofstream odp;

int Cards[5][5];
int answer1[5], answer2[5];

void read_data(){
    int VolunteerNumber;
    cin >> VolunteerNumber;

    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            cin >> Cards[i][j];

    for (int i=1; i<=4; i++)
        answer1[i] = Cards[VolunteerNumber][i];

    cin >> VolunteerNumber;

    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            cin >> Cards[i][j];

    for (int i=1; i<=4; i++)
        answer2[i] = Cards[VolunteerNumber][i];
}

void program(int TestNumber){
    read_data();
    bool GotAnswer = false;
    int answer;
    for (int i=1; i<=4; i++){
        for (int j=1; j<=4; j++){
            if (answer1[i] == answer2[j]){
                if (GotAnswer == true){
                    odp << "Case #" << TestNumber << ": Bad magician!\n";
                    return;
                }

                GotAnswer = true;
                answer = answer1[i];
            }
        }
    }

    if (GotAnswer == false){
        odp << "Case #" << TestNumber << ": Volunteer cheated!\n";
        return;
    }

    odp << "Case #" << TestNumber << ": " << answer << "\n";
}

int main(){
    int T;
    cin >> T;
    odp.open("/home/staniul/Desktop/Google Code Jam/ODP.in");
    for (int i=1; i<=T; i++){
        program(i);
    }
    odp.close();

    return 0;
}
