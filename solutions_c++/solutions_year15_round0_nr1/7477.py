
#ifndef jam_util_h
#define jam_util_h

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

class Util {
public:
    // ====================================================================================================
    static std::vector<std::string> split(const std::string & str);
    // ====================================================================================================
    static void strech_left(std::string & str, char c, size_t final_size);
    // ====================================================================================================
    static std::string strech_left_copy(std::string str, char c, size_t final_size);
    // ====================================================================================================
    template<typename T>
    static std::vector<T> reverse(const std::vector<T> & in) {
        std::vector<T> out;
        out.reserve(in.size());
        for (auto i = in.rbegin(); i != in.rend(); ++i) {
            out.push_back(*i);
        }
        return out;
    }
    // ====================================================================================================
    template<typename T>
    static void ascend(std::vector<T> & in) {
        std::sort(in.begin(), in.end());
    }
    // ====================================================================================================
    template<typename T>
    static void descend(std::vector<T> & in) {
        std::sort(in.begin(), in.end(), std::greater<T>());
    }
    // ====================================================================================================
    template<typename T>
    static T read(std::istream & in) {
        T t;
        in >> t;
        return t;
    }
    // ====================================================================================================
    template<typename T>
    static void print(std::ostream & out, const std::vector<T> & vec) {
        for (const auto & t : vec) {
            out << t << " ";
        }
        out << std::endl;
    }
    // ====================================================================================================
    template<typename T>
    static std::vector<T> readVector(std::istream & in, const size_t N) {
        std::vector<T> result;
        result.reserve(N);
        for (size_t i = 0; i < N; ++i) {
            T n;
            in >> n;
            result.push_back(n);
        }
        return result;
    }
    // ====================================================================================================
    static void skipLine(std::istream & in);
};
#endif
