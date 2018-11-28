#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int t;
    cin >> t;ofstream outfile;
    outfile.open("output.txt");
    int counr(0);
    for (counr=1;counr<=t;counr++){
           int done(0);
            char array[5][4];
    int c1(0);
    for (c1=0;c1<4;c1++){cin>>array[c1];}
    int c2(0),o(0),x(0);
    for (c2=0;c2<4;c2++){
    for (c1=0;c1<3;c1++){
        if (array[c2][c1]=='T' || array[c2][c1]=='O')o++;
    if (array[c2][c1]=='T' || array[c2][c1]=='X')x++;}
    if (array[c2][3]=='T' || array[c2][3]=='X'){x++;}
    if (array[c2][3]=='O' || array[c2][3]=='O'){o++;}
    if (x==4){outfile << "Case #" << counr << ": " << "X won";done++;goto label;}x=0;
    if (o==4){outfile << "Case #" << counr << ": " <<"O won";done++;}o=0;
    }
    label:;x=0;o=0;
    int c3(0);
    for (c3=0;c3<4;c3++){
     for (c2=0;c2<4;c2++){
        if (array[c2][c3]=='T' || array[c2][c3]=='O')o++;
if (array[c2][c3]=='T' || array[c2][c3]=='X')x++;
     }
     if (x==4 && done==0){outfile << "Case #" << counr << ": " << "X won";done++;goto label1;}x=0;
    if (o==4 && done==0){outfile << "Case #" << counr<< ": " <<"O won";done++;}o=0;
    }
    label1:;x=0;o=0;
    int c5(0),c6(3);
    for (c5=0;c5<3;c5++){if (array[c5][c5]=='T' || array[c5][c5]=='O')o++; else if (array[c5][c5]=='T' || array[c5][c5]=='X')x++;}

    if (array[3][3]=='T' || array[3][3]=='X')x++; else if (array[3][3]=='T' || array[3][3]=='O')o++;
    if (x==4&&done==0){outfile << "Case #" << counr << ": " << "X won";done++;goto label2;}x=0;
    if (o==4&&done==0){outfile << "Case #" << counr << ": " << "O won";done++;}o=0;
    label2:;x=0;o=0;
    int c8(0),c7(3);
    for (c8=0;c8<3;c8++){
            if (array[c8][c7]=='T' || array[c8][c7]=='O')o++; else if (array[c8][c7]=='T' || array[c8][c7]=='X')x++;c7--;
    }
    if (array[3][0]=='T' || array[3][0]=='O')o++;
    if (array[3][0]=='T' || array[3][0]=='X')x++;

    if (x==4&&done==0){outfile << "Case #" << counr << ": " << "X won";done++;goto label4;}x=0;
    if (o==4&&done==0){outfile << "Case #" << counr << ": " << "O won";done++;}o=0;
    label4:;x=0;o=0;
    if (done==0){
            int dot(0),blnk(0);
        int c7(0);
        for (c7=0;c7<4;c7++){
            int cg(0);
            for (cg=0;cg<4;cg++){if (array[c7][cg]=='.')dot++; else blnk++;}
        }

    if (dot!=0){outfile << "Case #" << counr << ": " << "Game has not completed"; } else {outfile << "Case #" << counr<< ": " << "Draw";}
    }
    outfile<<endl;
    }
outfile << endl;
return 0;
}
