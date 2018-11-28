//================================================================================================//
//  powers.h
//  GoogleCodeJam
//
//  Created by Zachary Clawson on 3/17/16.
//  Copyright © 2016 Zachary_Clawson. All rights reserved.
//================================================================================================//

#ifndef powers_h
#define powers_h

namespace custom_math {

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

template <class T>
T square(const T n) {
    return n * n;
}

using IntegerType = long int;

//template <class IntegerType>
constexpr IntegerType pow2(const IntegerType power) {
    return (power == 0) ? 1 : 2 * pow2(power - 1);
}

//template <class IntegerType>
constexpr IntegerType pow3(const IntegerType power) {
    return (power == 0) ? 1 : 3 * pow3(power - 1);
}

template <class ReturnType, class PowerType>
constexpr
ReturnType pow10(const PowerType power) {
    return (power == 0) ? 1 : pow10<ReturnType,PowerType>(power - 1) * 10;
}

template <class ReturnType, class PowerType>
ReturnType InfInt_pow10(const PowerType power) {
    return (power == 0) ? 1 : pow10<ReturnType,PowerType>(power - 1) * 10;
}

/** Computes base^exp mod modulus
 *
 */
template <typename T1, typename T2, typename T3>
T1 modpow(T1 base, T2 exp, const T3 modulus) {
    base %= modulus;
    T1 result = 1;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % modulus;
        base = (base * base) % modulus;
        exp >>= 1;
    }
    return result;
}

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

} // custom_math

#endif /* powers_h */
