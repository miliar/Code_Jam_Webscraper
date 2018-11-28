#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    ifstream ifs("in.in");
    ofstream ofs("out.out");

    int T;
    ifs >> T;
    for (int t = 1; t <= T; ++t) {
        int N;
        ifs >> N;

        vector<string> cars;
        for (int i = 0; i < N; ++i) {
            string car;
            ifs >> car;
            cars.push_back(car);
        }

        ofs << "Case #" << t << ": ";

        int possibility = 1;
        bool valid = true;
        for (char c = 'a'; c <= 'z' && valid; ++c) {
            int beginIndex = -1;
            int beginCount = 0;
            int midCount = 0;
            int endIndex = -1;
            int endCount = 0;
            int pureCount = 0;
            int pureLength = 0;

            for (int i = cars.size() - 1; i >= 0 && valid; --i) {
                string &car = cars[i];
                size_t p1 = car.find_first_of(c);
                size_t p2 = car.find_last_of(c);

                if (p1 == string::npos) {
                    continue;
                }

                for (size_t p = p1; p <= p2; ++p) {
                    if (car[p] != c) {
                        valid = false;
                        break;
                    }
                }

                if (valid) {
                    if (p1 == 0 && p2 < car.length() - 1) {
                        if (beginCount == 0) {
                            ++beginCount;
                            beginIndex = i;
                        } else {
                            valid = false;
                        }
                    } else if (p1 > 0 && p2 == car.length() - 1) {
                        if (endCount == 0) {
                            ++endCount;
                            endIndex = i;
                        } else {
                            valid = false;
                        }
                    } else if (p1 == 0 && p2 == car.length() - 1) {
                        ++pureCount;
                        pureLength += p2 - p1 + 1;
                        cars.erase(cars.begin() + i);

                        if (beginIndex != -1) {
                            --beginIndex;
                        }
                        if (endIndex != -1) {
                            --endIndex;
                        }
                    } else {
                        ++midCount;
                    }
                }
            }

            if (valid) {
                if (beginCount > 1 || endCount > 1) {
                    valid = false;
                }
                if ((beginCount > 0 || endCount > 0 || pureLength > 0) && midCount > 0) {
                    valid = false;
                }
            }

            if (valid && (beginCount > 0 || pureCount > 0 || endCount > 0)) {
                for (int i = 2; i <= pureCount; ++i) {
                    possibility *= i;
                }
                string pureStr(pureLength, c);
                string beginStr;
                if (beginIndex != -1) {
                    beginStr = cars[beginIndex];
                }
                string endStr;
                if (endIndex != -1) {
                    endStr = cars[endIndex];
                }
                ostringstream oss;
                oss << endStr << pureStr << beginStr;
                if (beginIndex < endIndex) {
                    if (endIndex != -1) {
                        cars.erase(cars.begin() + endIndex);
                    }
                    if (beginIndex != -1) {
                        cars.erase(cars.begin() + beginIndex);
                    }
                } else {
                    if (beginIndex != -1) {
                        cars.erase(cars.begin() + beginIndex);
                    }
                    if (endIndex != -1) {
                        cars.erase(cars.begin() + endIndex);
                    }
                }
                //cout << c << " -> " << oss.str() << endl;
                cars.push_back(oss.str());
            }
        }

        if (valid) {
            for (int i = 2; i <= cars.size(); ++i) {
                possibility *= i;
            }
            ofs << possibility << endl;
        } else {
            ofs << 0 << endl;
        }
    }

    return 0;
}
