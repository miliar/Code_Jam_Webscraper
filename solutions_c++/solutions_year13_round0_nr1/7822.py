#include <cstdio>
#include <iostream>
 
using namespace std;
 
int v1,v2,v3,v4;
int h1,h2,h3,h4;
int c1,c2;
bool incomplete;
bool draw;
 
void game_finish (int val) {
        if ((val&0x0F) == 0x0F) {
            cout << "X won" << endl; draw = false; return ;
        } else {
            cout << "O won" << endl; draw = false; return ;
        }

}
 
int check (int p, char c, int v)
{
    int retval = v;
//printf("%x(%d,%c),", v,p,c);
    if (c == 'T') {
        retval = retval | (1 << (p-1));
        retval = retval | (1 << (p+3));
    } else if (c == 'X') {
        retval = retval | (1 << (p-1));
    } else if (c == 'O') {
        retval = retval | (1 << (p+3));
    } else {
        incomplete = true;
    }
//printf("%x,", retval);
    return retval;
}
 

int main(void)
{
    string line = "";
    int linenum = 0;
    cin >> linenum;
    for (int i = 0; i < linenum; ++i) {
        string line1, line2, line3, line4;
        v1 = v2 = v3 = v4 = h1 = h2 = h3 = h4 = c1 = c2 = 0;
        incomplete = false;
        draw = true;
        
        cin >> line1;
        if (line1.size() != 4) { continue; }
        cin >> line2; cin >> line3; cin >> line4;
        
        cout << "Case #" << (i+1) << ": ";
        
        h1 = check (1, line1[0], h1);
        h1 = check (2, line1[1], h1);
        h1 = check (3, line1[2], h1);
        h1 = check (4, line1[3], h1);
        if ((h1&0x0F) == 0x0F || (h1&0xF0) == 0xF0) { game_finish(h1);}
        if (!draw) {continue;} 
 
        h2 = check (1, line2[0], h2);
                h2 = check (2, line2[1], h2);
                h2 = check (3, line2[2], h2);
                h2 = check (4, line2[3], h2);
                if ((h2&0x0F) == 0x0F || (h2&0xF0) == 0xF0) { game_finish(h2);}
        if (!draw) {continue;}
        
        h3 = check (1, line3[0], v1);
                h3 = check (2, line3[1], v1);
                h3 = check (3, line3[2], v1);
                h3 = check (4, line3[3], v1);
                if ((h3&0x0F) == 0x0F || (h3&0xF0) == 0xF0) { game_finish(h3);}
        if (!draw) {continue;}
 
        h4 = check (1, line4[0], v1);
                h4 = check (2, line4[1], v1);
                h4 = check (3, line4[2], v1);
                h4 = check (4, line4[3], v1);
                if ((h4&0x0F) == 0x0F || (h4&0xF0) == 0xF0) { game_finish(h4);}
        if (!draw) {continue;}
 
 
        v1 = check (1, line1[0], v1);
                v1 = check (2, line2[0], v1);
                v1 = check (3, line3[0], v1);
                v1 = check (4, line4[0], v1);
                if ((v1&0x0F) == 0x0F || (v1&0xF0) == 0xF0) { game_finish(v1);}
        if (!draw) {continue;}
 
        v2 = check (1, line1[1], v2);
                v2 = check (2, line2[1], v2);
                v2 = check (3, line3[1], v2);
                v2 = check (4, line4[1], v2);
                if ((v2&0x0F) == 0x0F || (v2&0xF0) == 0xF0) { game_finish(v2);}
        if (!draw) {continue;}
 
        v3 = check (1, line1[2], v3);
                v3 = check (2, line2[2], v3);
                v3 = check (3, line3[2], v3);
                v3 = check (4, line4[2], v3);
                if ((v3&0x0F) == 0x0F || (v3&0xF0) == 0xF0) { game_finish(v3);}
        if (!draw) {continue;}
 
        v4 = check (1, line1[3], v4);
                v4 = check (2, line2[3], v4);
                v4 = check (3, line3[3], v4);
                v4 = check (4, line4[3], v4);
                if ((v4&0x0F) == 0x0F || (v4&0xF0) == 0xF0) { game_finish(v4);}
        if (!draw) {continue;}
 
        c1 = check (1, line1[0], c1);
                c1 = check (2, line2[1], c1);
                c1 = check (3, line3[2], c1);
                c1 = check (4, line4[3], c1);
                if ((c1&0x0F) == 0x0F || (c1&0xF0) == 0xF0) { game_finish(c1);}
        if (!draw) {continue;}
 
        c2 = check (1, line1[3], c2);
                c2 = check (2, line2[2], c2);
                c2 = check (3, line3[1], c2);
                c2 = check (4, line4[0], c2);
                if ((c2&0x0F) == 0x0F || (c2&0xF0) == 0xF0) { game_finish(c2);}
        if (!draw) {continue;}
        
        if (!incomplete) {
            cout << "Draw" << endl;
        } else {
            cout << "Game has not completed" << endl;
        }
 
    }
    return 0;
}
