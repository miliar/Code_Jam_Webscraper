// Copyright (c) 2016 olibre <olibre@Lmap.org>
//
// This file is licensed under the 'Fair License'
// except the function `ostream& operator<<(ostream&,__uint128_t)`
// that is a copy from http://stackoverflow.com/a/25115163/938111
//
// Fair License:   Usage of the works is permitted provided
//                 that this instrument is retained with the works,
//                 so that any entity that uses the works
//                 is notified of this instrument.
//                 DISCLAIMER: THE WORKS ARE WITHOUT WARRANTY.
//
// Possible French translation:
//
//                 Les oeuvres peuvent etre reutilisees
//                 a condition d'etre accompagnees du texte de cette licence,
//                 afin que tout utilisateur en soit informe'.
//                 AVERTISSEMENT : LES OEUVRES N'ONT AUCUNE GARANTIE.
//
// Extract of the GOOGLE CODE JAM TERMS AND CONDITIONS
// accepted by olibre in order to participate to the contest:
//
// 8. Ownership; Rights in Your Submissions; Privacy.
//  8.3 License to Submissions.
//      For any submission you make to the Contest,
//      you grant Google a non-exclusive, worldwide, perpetual, irrevocable,
//      free license (with the right to sublicense) to reproduce,
//      prepare derivative works of, distribute, publicly perform,
//      publicly display, and otherwise use such submission for the purpose
//      of administering and promoting the Contest.
//      Your submitted source code may be made available for anyone
//      to view on the Internet and download and use at the end of the Contest.

#include <iostream>
#include <stdint.h> // uint_fast64_t
#include <string>
#include <cassert>
#include <limits>
#include <iomanip>
#include <vector>
#include <cmath>
#include <iterator> // std::end()
#include <map>

using namespace std;

void process (const std::string& word)
{
    std::map<char,int> letters;
    std::map<char,int> result;

    for (auto e: word)
    {
        switch (e)
        {
        case 'Z':
            --letters['O'];
            ++result['0'];
            break;

        case 'W':
            --letters['O'];
            ++result['2'];
            break;

        case 'U':
            --letters['F'];
            --letters['O'];
            ++result['4'];
            break;

        case 'X':
            --letters['S'];
            ++result['6'];
            break;

        case 'G':
            --letters['H'];
            ++result['8'];
            break;

        default:
            ++letters[e];
        }
    }

    if (letters['H'])    result['3']  += letters['H'];

    if (letters['F'])    result['5']  += letters['F'];

    if (letters['S']) {  result['7']  += letters['S'];
                         letters['N'] -= letters['S']; }

    if (letters['O']) {  result['1']  += letters['O'];
                         letters['N'] -= letters['O']; }

    for (auto e: result)
    {
        if (e.second)
        {
            std::cout << std::string( e.second, e.first );
        }
    }

    {
        int count = letters['N'];
        if (count)
        {
            assert(count%2 == 0);
            std::cout << std::string( count/2, '9' );
        }
    }
}


int main()
{
//    process ("ETHER");
//    return 0;


    int t;  std::cin >> t;
    assert (t >= 0  );
    assert (t <= 100);

    for (int i=1; i<=t; ++i)
    {
        std::cout <<"Case #"<< i <<": ";

        std::string word;
        std::cin >> word;

        process (word);

        std::cout << std::endl;
    }
}
