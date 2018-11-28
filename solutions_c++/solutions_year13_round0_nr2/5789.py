#include <iostream>

using namespace std;

int main() {
    int ncases;
    cin>>ncases;
    for(int caseNum=0; caseNum < ncases; caseNum++) {
        int length, width;
        int heights[100][100], maxHeightInRow[100], maxHeightInCol[100];
        cin>>length>>width;
        for(int j=0; j<width; j++) {
            maxHeightInCol[j] = -1;
        }
        for(int i=0; i<length; i++) {
            maxHeightInRow[i] = -1;
            for(int j=0; j<width; j++) {
                cin>>heights[i][j];
                if(heights[i][j] > maxHeightInRow[i])
                    maxHeightInRow[i] = heights[i][j];
                if(heights[i][j] > maxHeightInCol[j])
                    maxHeightInCol[j] = heights[i][j];
            }
        }
        bool good = true;
        for(int i=0; i<length; i++) {
            for(int j=0; j<width; j++) {
                if(maxHeightInRow[i] != heights[i][j] && maxHeightInCol[j] != heights[i][j]) {
                    good = false;
                    break;
                }
            }
        }
        cout<<"Case #"<<caseNum+1<<": "<<(good?"YES":"NO")<<"\n";
    }
}