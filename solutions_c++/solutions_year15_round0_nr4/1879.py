#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <tuple>

const std::string PICKER { "RICHARD" };
const std::string PLACER { "GABRIEL" };

std::string solve(size_t omnino_area, size_t rect_height, size_t rect_width)
{
    // Area >= 7  => picker can use a piece with an 1x1 hole which cannot be filled
    if (7 < omnino_area)
    {
        return PICKER;
    }

    // omnio all in one row > rect?
    if (omnino_area > std::max(rect_height, rect_width))
    {
        return PICKER;
    }

    // not fillable
    if (0 != (rect_height * rect_width) % omnino_area)
    {
        return PICKER;
    }

    // does right angle omnio fit?
    size_t right_angle_side = (omnino_area + 1) / 2;
    if (right_angle_side > std::min(rect_height, rect_width))
    {
        return PICKER;
    }
    
    std::tie(rect_height, rect_width) = std::minmax(rect_height, rect_width);
    // Special cases: unfillable space
    // only for N-omnios with N = 4, 5, 6
    // n=4: Height 2: Split: 1/1 always separates into 2 parts with odd area
    //  X 
    // XXX

    // n=5: Split: 1/3
    // X
    // XX
    //  XX
    //  - 1/3: Width = 5

    // n=6: Split: 2/4
    // XXXX
    //  X
    //  X
    //  - 2/4: independent of width (no part divisble by 3)
    if ((4 == omnino_area && 2 == rect_height)
        || (5 == omnino_area && 3 == rect_height && 5 == rect_width)
        || (6 == omnino_area && 3 == rect_height)
        )
    {
        return PICKER;
    }

    return PLACER;
}

int main(int argc, char** argv)
{
    if (2 > argc)
    {
        std::cerr << argv[0] << " inputfile [outputfile]" << std::endl;
        return 1;
    }
    std::string infile{argv[1]};
    std::string outfile{infile};
    if (2 < argc)
    {
        outfile = argv[2];
    }
    else
    {
        outfile += ".out";
    }

    std::ifstream in(infile);
    std::ofstream out(outfile);
    if (!in.good())
    {
        std::cerr << "Bad input file" << std::endl;
        return 2;
    }

    if (!out.good())
    {
        std::cerr << "Bad output file" << std::endl;
        return 3;
    }

    int cases;
    in >> cases;

    for (int caseno = 1; caseno <= cases; ++caseno)
    {
        size_t omnino_area, rect_height, rect_width;
        in >> omnino_area >> rect_height >> rect_width;
        
        out << "Case #" << caseno << ": " << solve(omnino_area, rect_height, rect_width) << std::endl;
    }
    out.flush();
}
