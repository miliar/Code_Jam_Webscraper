//
//  main.cpp
//
//  Google Code Jam 2k15 - Round 0 - Problem D
//

// Yes, I did this in a really dumb way as far as flags and jumps...
// Also, reading the problem wrong was a mistake -- Gabriel can use *any* x-ominos.


#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    int cases, current;
    int x, r, c;
    int canmangle, leg;
    
    std::cin >> cases;
    for (current=1; current<=cases; ++current) {
        std::cout << "Case #" << current << ": ";
        std::cin >> x;
        std::cin >> r;
        std::cin >> c;
        canmangle = 0;
        
        if (x == 1) goto skip; // trivial win for G
        if ((r<x) && (c<x)) {canmangle = 1; goto skip;} // straight line

        leg = x/2 + 1; // enforcing headroom for weird shapes...  works out?
        if (((x>2) && ((r<leg) || (c<leg)))) {canmangle = 1; goto skip;} // worst case L

        // 4 z or t need 2 other 4-ominos
        
        // 5-arch needs 2 other 5-ominos...  but already accounted for by above
        // 5-uneven cross...  can rotate! still ok!
        
        // 6-wishbone needs 3+1 both dimensions for the gap
        // or specifically 3 other 6-ominos for gap + hip-pits.
        
        if (x>6) {canmangle = 1; goto skip;} // 7-omino can wrap hole
        canmangle = (((r*c) % x) ? 1 : 0);
        
        
    skip:
        std::cout << (canmangle ? "RICHARD" : "GABRIEL") << std::endl;
    }
}

