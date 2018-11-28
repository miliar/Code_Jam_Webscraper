//
// Created by Thanadee on 11/16/2015.
//

#ifndef TEST_NATIVE_MACRO_H
#define TEST_NATIVE_MACRO_H

#define TNDLOG std::cout << __FILE__ << " at line " << __LINE__ << " :" << std::endl

template<typename T>
struct MoveReference{
    using type = T;
};
template<typename T>
struct MoveReference<T&>{
    using type = T&;
};
template<typename T>
struct MoveReference<T const&>{
    using type = T;
};
template<typename T>
struct MoveReference<T&&>{
    using type = T;
};


#define ifMacroGuard if(false){}else
#define macroScope(i,v) if(bool i##Scope = true) for(MoveReference<decltype((v))>::type i = v; i##Scope; i##Scope = false)
#define fore(var,collection) ifMacroGuard macroScope(var##Collection, collection)\
    for (auto var = var##Collection.begin(), var##End = var##Collection.end(); var != var##End; ++var)
#define fori(i,n) for(decltype(n) i = 0, iEnd = n; i < iEnd; ++i)
#define ifMapContain(i,map,val) macroScope(i##mapRef,map) macroScope(i, i##mapRef.find(val)) if(i##mapRef.end() != i)


#ifdef DEBUG

#define LOGVAR(var) TNDLOG << #var << " = " << var << std::endl;
#define D(x) x

#else
#define LOGVAR(var)
#define D(x)
#endif

#ifndef _MSC_VER
#define NOEXCEPT noexcept
#else
#define NOEXCEPT
#endif

#define EXCEPTION_TYPE(typeName,str)\
class typeName : public std::exception{\
public:\
	char const* what() const NOEXCEPT{\
		return #typeName ":" str;\
	}\
};

#endif //TEST_NATIVE_MACRO_H
