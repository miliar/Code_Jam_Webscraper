#include <iostream>
#include <fstream>
using namespace std;
ofstream out("output.txt");

int lawn[100][100], width, height, cases;
bool seen[100][100];

int main(){
    cin>>cases;
    for(int c = 1; c <= cases; c++){
        cin>>height>>width;
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                cin>>lawn[i][j];
                seen[i][j] = false;
            }
        }
        bool possible = true, done = false;
        while(possible&&!done){
            int lowest = (1<<30), lowestY, lowestX;
            // find lowest
            for(int i = 0; i < height; i++) for(int j = 0; j < width; j++){
                if(!seen[i][j] && lawn[i][j] < lowest){
                    lowest = lawn[i][j];
                    lowestX = j; lowestY = i;
                }
            }
            if(lowest == (1<<30)){
                    done = true;
            }else{
                // try vertically and horizontally
                bool vert = true, hori = true;
                for(int j = 0; j < width; j++){
                    if(!seen[lowestY][j] && lawn[lowestY][j] > lowest) hori = false;
                }
                for(int i = 0; i < height; i++){
                    if(!seen[i][lowestX] && lawn[i][lowestX] > lowest) vert = false;
                }
                if(hori){
                    // flatten horizontal
                    for(int i = 0; i < width; i++) seen[lowestY][i] = true;
                }
                if(vert) for(int i = 0; i < height; i++) seen[i][lowestX] = true;
                if(!hori&&!vert) possible = false;
            }
        }
        out<<"Case #"<<c<<": "<<(possible?"YES\n":"NO\n");

    }
}
