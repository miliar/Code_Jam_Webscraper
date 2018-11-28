

    //
    //  main.cpp
    //  SECOND
    //
    //  Created by Abhishek Anand on 13/04/14.
    //  Copyright (c) 2014 AbhishekAnand. All rights reserved.
    //

    #include <iostream>
    #include <iomanip>
    #include <fstream>
    using namespace std;
    int main(int argc, const char * argv[])
    {
        ofstream out ("B.txt");
        int n;
        cin >> n;
        for(int i = 1; i <=n; i++){



            double c, f, x;

            cin >> c >> f >> x;
            double time, timebefore, speed, realtime;


            timebefore = x/2;
            time= (c/2);

            speed = 2 + f;
            realtime = time+(x/speed);
            while(realtime < timebefore){
                timebefore = realtime;
                time = time + (c/speed);
                speed = speed + f;
                realtime = time + x/speed;
            }
            out <<  "Case #" << i << ": " << setprecision(12) << timebefore << "\n";
        }
        out.close();
        return 0;
    }

