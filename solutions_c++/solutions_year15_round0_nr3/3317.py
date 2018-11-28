/*
 *  Created on: Apr 11, 2015
 *      Author: gustavo
 */

#ifndef DIJKSTRA_H_
#define DIJKSTRA_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <assert.h>
#include <fstream>
#include <utility>
#include <iostream>
#include <stdexcept>

#include <vector>
#include <queue>
#include <algorithm>

class Dijkstra {
public:
    int hash(char a, bool minus) {
        int result = minus ? 4 : 0;
        if (a == '1') {
            return result;
        }
        if (a == 'i') {
            return result + 1;
        }
        if (a == 'j') {
            return result + 2;
        }
        return result + 3;
    }
    void multiply(char& a, char b, bool& minus) {
        if (a == '1') {
            if      (b == '1') { a = '1';}
            else if (b == 'i') { a = 'i';}
            else if (b == 'j') { a = 'j';}
            else if (b == 'k') { a = 'k';}
        } else if (a == 'i') {
            if      (b == '1') { a = 'i';}
            else if (b == 'i') { a = '1'; minus = !minus;}
            else if (b == 'j') { a = 'k';}
            else if (b == 'k') { a = 'j'; minus = !minus;}
        } else if (a == 'j') {
            if      (b == '1') { a = 'j';}
            else if (b == 'i') { a = 'k'; minus = !minus;}
            else if (b == 'j') { a = '1'; minus = !minus;}
            else if (b == 'k') { a = 'i';}
        } else if (a == 'k') {
            if      (b == '1') { a = 'k';}
            else if (b == 'i') { a = 'j';}
            else if (b == 'j') { a = 'i'; minus = !minus;}
            else if (b == 'k') { a = '1'; minus = !minus;}
        }
    }

    void backmultiply(char a, char& b, bool& minus) {
        if (a == '1') {
            if      (b == '1') { b = '1';}
            else if (b == 'i') { b = 'i';}
            else if (b == 'j') { b = 'j';}
            else if (b == 'k') { b = 'k';}
        } else if (a == 'i') {
            if      (b == '1') { b = 'i';}
            else if (b == 'i') { b = '1'; minus = !minus;}
            else if (b == 'j') { b = 'k';}
            else if (b == 'k') { b = 'j'; minus = !minus;}
        } else if (a == 'j') {
            if      (b == '1') { b = 'j';}
            else if (b == 'i') { b = 'k'; minus = !minus;}
            else if (b == 'j') { b = '1'; minus = !minus;}
            else if (b == 'k') { b = 'i';}
        } else if (a == 'k') {
            if      (b == '1') { b = 'k';}
            else if (b == 'i') { b = 'j';}
            else if (b == 'j') { b = 'i'; minus = !minus;}
            else if (b == 'k') { b = '1'; minus = !minus;}
        }
    }
    void main(std::string filePath, std::string outPath) {
        std::ifstream in;
        in.open(filePath.c_str());
        if (!in)
            throw std::runtime_error("Problem with file");
        std::cout << "\nProcessing " << filePath << "\n";
        std::ofstream out;
        out.open(outPath.c_str());

        int testCases;
        in >> testCases;
        std::cout << testCases << " test cases \n";
        std::string line;
        for (int testCase = 0; testCase < testCases; ++testCase) {
            int64_t L, X;
            in >> L;
            in >> X;
            getline(in, line);
            getline(in, line);

            std::cout << "Read " << L << " " << X << " " << line << "\n";

//            char a = '1';
//            bool minus = false;
//
//            int found = 0;
//            for (int i = 0; i < X; ++i) {
//                for(std::string::iterator it = line.begin(); it != line.end(); ++it) {
//                    multiply(a, *it, minus);
//                    if (found == 0 && a == 'i' && !minus) {
//                        found = 1;
//                        a = '1';
//                        minus = false;
//                    } else if (found == 1 && a == 'j' && !minus) {
//                        found = 2;
//                        a = '1';
//                        minus = false;
//                    }
//                }
//            }
//
//            bool ok = found == 2 && a == 'k' && !minus;


            char a = '1';
            bool minus = false;
            for(std::string::iterator it = line.begin(); it != line.end(); ++it) {
                multiply(a, *it, minus);
            }
            std::cout << "Result: " << (minus ? "-":"") << a << "\n";

            bool ok = (a != '1' && X >= 2 && (X - 2 ) % 4 == 0) || (a == '1' && minus && X % 2 == 1);

            if (ok) {
                // check if we can actuall make the letters

                // check i
                a = '1';
                minus = false;
                int ijcount = 1;
                bool ifound = false;
                bool jfound = false;
                for (int i = 0; i < 8; i++) {
                    for(std::string::iterator it = line.begin(); it != line.end(); ++it) {
                        multiply(a, *it, minus);
                        if (!ifound) {
                            if (a == 'i' && !minus) {
                                ifound = true;
                                a = '1';
                                minus = false;
                                std::cout << "Found i\n";
                            }
                        } else {
                            if (a == 'j' && !minus) {
                                jfound = true;
                                std::cout << "Found j\n";
                                break;
                            }
                        }
                        ijcount++;
                    }
                    if (ifound && jfound) break;
                }
                bool kfound = false;
                int kcount = 1;
                if (ifound && jfound) {
                    char b = '1';
                    minus = false;
                    for (int i = 0; i < 4; i++) {
                        for(int j = line.size() - 1; j >= 0; --j) {
                            std::cout << "Trying: " << j << ": " << line[j] << "\n";
                            backmultiply(line[j], b, minus);
                            if (b == 'k' && !minus) {
                                kfound = true;
                                std::cout << "Found k\n";
                                break;
                            }
                            kcount++;
                        }
                        if (kfound) break;
                    }
                }
                std::cout << "Sum: " << ijcount + kcount << " has to be smaller or equal to " << L*X << "\n";
                ok = ifound && jfound && kfound && ijcount + kcount <= L*X;
            }



            std::cout << "Case #" << testCase + 1 << ": " << (ok ? "YES" : "NO") << "\n";
            out << "Case #" << testCase + 1 << ": " << (ok ? "YES" : "NO") << "\n";
        }

    }

};

#endif /* STANDINGOVATION_H_ */
