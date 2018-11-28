#include <cstdlib>
#include <stdio.h>
#include <string.h>

#include <iostream>
#include <sstream>
#include <string>


using namespace std;

typedef unsigned char byte;

class Lawn {

    public:
        Lawn(byte n, byte m);
        ~Lawn();
        
        void update(byte line, char* buffer);
        string canCut();
        
    private:
        char valid(byte y, byte x);
        
        byte n,m;
        byte** lawn;
        
        static const string YES;
        static const string NO;
};

const string Lawn::YES = "YES";
const string Lawn::NO  = "NO";

Lawn::Lawn(byte n, byte m) {
    this->n = n;
    this->m = m;
    
    lawn = (byte **) malloc(n*sizeof(byte *));
    for (int i = 0; i < n; i++) {
        lawn[i] = (byte *) malloc(m*sizeof(byte));
    }
}

Lawn::~Lawn() {
    for (byte i = 0; i < n; i++) {
        free(lawn[i]);
    }
    free(lawn);
}

string Lawn::canCut() {
    
    for (byte y = 0; y < n; y++) {
        for (byte x = 0; x < m; x++) {
            if (!valid(y, x)) {
                return NO;
            }
        }
    }
    return YES;
}

char Lawn::valid(byte _y, byte _x) {

    byte horz_flag = 0;
    byte vert_flag = 0;
    
    // horizontal
    for (int x = 0; x < m; x++) {
        if (x != _x) {
            if (lawn[_y][x] > lawn[_y][_x]) {
                horz_flag = 1;
                break;
            }
        }
    }
    // vertical
    for (int y = 0; y < n; y++) {
        if (y != _y) {
            if (lawn[y][_x] > lawn[_y][_x]) {
                vert_flag = 1;
                break;
            }
        }
    }
    
    return !(horz_flag & vert_flag);
}

void Lawn::update(byte line, char* buffer) {
    string token;
    string raw(buffer);
    istringstream iss(raw);
    
    char x = 0;
    do {
        iss >> token;
        lawn[line][x++] = atoi(token.c_str());
    } while (iss && x < m);
}

int main(int argc, char** argv) {

    //freopen("in", "r", stdin);
    
    int i,line,T;
    int n,m;
    Lawn* lawn;
    char* buffer = (char *) malloc(500*sizeof(char));
    
    scanf("%d\n", &T);
    
    for (i = 0; i < T; i++) {
        scanf("%d %d\n", &n, &m);
        lawn = new Lawn(n, m);
        
        for (line = 0; line < n; line++) {
            memset(buffer, ' ', 30*sizeof(char));
            scanf("%[^\t\n]\n", buffer);
            
            lawn->update(line, buffer);
        }
        
        printf("Case #%d: %s\n", i+1, lawn->canCut().c_str());
    }
    
    return 0;
}

