#include <iostream>
#include <vector>

using namespace std;

void lawnmower(vector<vector<int> > grid);
bool possible(vector<vector<int> > grid, int x, int y);

bool checkVertical(vector<vector<int> > grid, int value, int x);
bool checkHorizontal(vector<vector<int> > grid, int value, int y);

int main() {
    int nCases;
    cin >> nCases;
    
    int width,height;
    
    for(int i=0;i<nCases;i++) {
        cin >> height;
        cin >> width;
        
       
        vector<vector<int> > grid(height, vector<int>(width));
        
        for(int y = 0; y < height;y++)
            for(int x = 0; x < width;x++)
                cin >> grid[y][x];
                
        cout << "Case #" << i+1 << ": "; 
        lawnmower(grid);
        cout << endl;
    }
    
    return 0;   
}


void lawnmower(vector<vector<int> > grid) {
    bool okay=true;
    for(int y=0;y<grid.size();y++) 
        for(int x=0;x<grid[y].size();x++) 
            if(!possible(grid,x,y))
                okay=false;
        
    if(okay)
        cout << "YES";
    else
        cout << "NO";
}


bool possible(vector<vector<int> > grid, int x, int y) {
    return checkVertical(grid,grid[y][x],x) || checkHorizontal(grid,grid[y][x],y);
}

bool checkVertical(vector<vector<int> > grid, int value, int x) {
    for(int y=0;y<grid.size();y++) 
        if(grid[y][x] > value)
            return false;
    
    return true;
}

bool checkHorizontal(vector<vector<int> > grid, int value, int y) {
    for(int x=0;x<grid[y].size();x++) 
        if(grid[y][x] > value)
            return false;
    
    return true;
}

