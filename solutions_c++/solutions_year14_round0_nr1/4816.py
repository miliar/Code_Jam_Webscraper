#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
using namespace std;

void readArray(string line, int n, int* store);

int main()
{
    std::ifstream in("A-small-attempt0.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    //ifstream infile("A-large-practice.in");
    //ofstream outfile;
    //outfile.open("out.txt", ofstream::out);
    //string line;

    //number of case
    //getline(infile, line);
    int ncase;
    cin >> ncase;
    //readArray(line, 1, &ncase);
    //cout << ncase;

    //system("pause");

    for(int i = 1; i<= ncase; i++){
        //getline(infile, line);
        int a1;
        cin >> a1;
        //readArray(line, 1, &credit);

        int temp[4];
        int r1[4];
        for(int row = 1; row <= 4; row++){
            if(row == a1)
                cin >> r1[0] >> r1[1] >> r1[2] >> r1[3];
            else
                cin >> temp[0] >> temp[1] >> temp[2] >> temp[3];
        }

        int a2;
        cin >> a2;
        //readArray(line, 1, &credit);

        int r2[4];
        for(int row = 1; row <= 4; row++){
            if(row == a2)
                cin >> r2[0] >> r2[1] >> r2[2] >> r2[3];
            else
                cin >> temp[0] >> temp[1] >> temp[2] >> temp[3];
        }

//        for (int j=0;j<4;j++) cout << r1[j] << ' ';
//        cout << endl;
//        for (int j=0;j<4;j++) cout << r2[j] << ' ';
//        cout << endl;

        int nOverlap = 0;
        int answer;
        for (int x=0;x<4;x++){
            int anchor = r1[x];
            for(int y=0;y<4; y++){
                if(r2[y]==anchor){
                    nOverlap++;
                    answer = anchor;
                    break;
                }
            }
        }
        //cout << nOverlap << ' ' << answer << endl;
        if(nOverlap == 1)
            cout << "Case #" << i << ": " << answer << endl;
        else if(nOverlap == 0)
            cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
        else
            cout << "Case #" << i << ": " << "Bad magician!" << endl;
    }

    return 0;
}

//void readArray(string line, int n, int* store)
//{
//    istringstream iss(line);
//    for(int i = 0; i<n; i++){
//        iss >> store[i];
//    }
//}
