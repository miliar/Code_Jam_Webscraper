

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input ("/Users/hasan/Desktop/xcode projects/magictrick/magictrick/A-small-attempt0.in.txt");
    ofstream output ("/Users/hasan/Desktop/xcode projects/magictrick/magictrick/A-small-attempt0.out.txt");
    
    int a[4][4], b[4][4];
    int t, i, j, m, n;
    input >> t;
    
    for (int l=0; l<t; l++) {
        input >> n;
        n--;
        for (i=0; i<4; i++)
            for (j=0; j<4; j++)
                input >> a[i][j];
        
        input >> m;
        m--;
        for (i=0; i<4; i++)
            for (j=0; j<4; j++)
                input >> b[i][j];
        
        int count = 0, c;
        for (i=0; i<4; i++)
            for (j=0; j<4; j++)
                if (a[n][i]==b[m][j])
                    count ++, c=a[n][i];
        if (count==1)
            output << "Case #" << l+1 << ": " << c << endl;
        else if (count==0)
            output << "Case #" << l+1 <<": Volunteer cheated!" << endl;
        else
            output << "Case #" << l+1 <<": Bad magician!" << endl;
    }
    
    return 0;
}
