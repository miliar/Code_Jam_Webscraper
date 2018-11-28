#include<fstream>

using namespace std;

int main() {
    int T,cards1[4][4],cards2[4][4],ans1,ans2,output,x,matches=0;;
    ifstream readinput;
    ofstream writeoutput;
    writeoutput.open("output.txt",ios::out|ios::app);
    readinput.open("A-small-attempt0.in",ios::in);
    readinput>>T;
    for(short i=1;i<=T;i++) {
        readinput>>ans1;
        matches=0;
        for(int j=0;j<4;j++) 
            for(int k=0;k<4;k++)
                readinput>>cards1[j][k];
        readinput>>ans2;
        for(int j=0;j<4;j++) 
            for(int k=0;k<4;k++)
                readinput>>cards2[j][k];
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                if(cards1[ans1-1][j]==cards2[ans2-1][k]) {
                    matches++;
                    output=cards1[ans1-1][j];
                }
                if(matches>1)
                    break;
            }
        }
        if(matches==1)
            writeoutput<<"Case #"<<i<<": "<<output<<endl;
        else if(matches<1)
            writeoutput<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        else
            writeoutput<<"Case #"<<i<<": Bad magician!"<<endl;
    }
    readinput.close();
    writeoutput.close();
    return 0;
}
